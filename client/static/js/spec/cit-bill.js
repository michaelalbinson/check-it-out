'use strict';


class CITBill extends _BaseDOM {
    constructor() {
        super();

        this.bootstrapStyles(true);
        this.getData();
    }

    getData() {
        const id = window.location.href.split('/').pop();
        request('/api/bill/' + id, {}, response => {
            this.render(response.data);
        }, err => {
            console.error('Error processing request!');
            console.error(err);
        }, request.METHODS.GET)
    }

    render(data) {
        this.appendChild(new ElementFactory(elements.H2, '', this._getTitle(data)));
        this.appendChild(new ElementFactory(elements.HR));
        this.appendChild(new ElementFactory());
        this.appendChild(new ElementFactory(elements.P, 'align-left', data.summary));
    }

    _getTitle(data) {
        return data.id.split('-')[0].toUpperCase() + ' - ' + (data.short_title || data.title);
    }
}

defineCustomElement('cit-bill', CITBill);