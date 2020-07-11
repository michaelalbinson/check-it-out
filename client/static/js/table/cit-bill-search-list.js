'use strict';


class CITBillSearchList extends ManagedTable {
    constructor() {
        super(CITBillSearchList.headers, '');
    }

    apiRequest(successCallback, errorCallback) {
        request('/api/bill/search/' + window.top.getURLParameter('q'), {}, successCallback, errorCallback, request.METHODS.GET);
    }

    getRow(dataRow, htmlRow) {
        let td = new ElementFactory(elements.TD);
        let linkElem = new ElementFactory(elements.A, '', '/bill/' + dataRow.id, dataRow.id.split('-')[0].toUpperCase());
        td.appendChild(linkElem);
        htmlRow.append(td);

        td = new ElementFactory(elements.TD, '', this._getAbbreviatedTitle(dataRow.short_title || dataRow.title));
        htmlRow.append(td);

        td = new ElementFactory(elements.TD, '', new Date(dataRow.introduced).toLocaleDateString());
        htmlRow.append(td);
    }

    /**
     *
     * @param row {object}
     * @param tags {array}
     * @returns {string}
     */
    getRowCorpusTerms(row, tags) {
        return (row.short_title + ' ' + row.state + ' ' + row.title + ' ' + row.summary).toLowerCase();
    }

    _getAbbreviatedTitle(potentialTitle) {
        if (potentialTitle && potentialTitle.length > 100)
            return potentialTitle.slice(0, 97) + '...';

        return potentialTitle;
    }
}

CITBillSearchList.headers = [
    {text: 'Bill Number', isOrderable: true, parameterMapping: 'title'},
    {text: 'Bill Title', isOrderable: true, parameterMapping: 'title'},
    {text: 'Introduced', isOrderable: true, parameterMapping: 'introduced'}
];

defineCustomElement('cit-bill-search-list', CITBillSearchList);