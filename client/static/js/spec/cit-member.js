'use strict';


class CITMember extends _BaseDOM {
    constructor() {
        super();

        this.bootstrapStyles(true);
        this.getData();
    }

    getData() {
        const id = window.location.href.split('/').pop();
        request('/api/member/' + id, {}, response => {
            this.render(response.data);
        }, err => {
            console.error('Error processing request!');
            console.error(err);
        }, request.METHODS.GET)
    }

    render(data) {
        console.log(data);
        let party = data.party;
        if (party === "D"){
            party = "Democrat";
        } else if (party === "R"){
            party = "Republican";
        } else{
            party = "Independent";
        }
        const image = ElementFactory(elements.IMG, '', '/assets/members/' + data.first_name.toLowerCase()
            + data.last_name.toLowerCase() + '.jpg');
        image.width = 150;
        this.appendChild(new ElementFactory(elements.H2, '', data.first_name + ' ' + data.last_name));
        this.appendChild(new ElementFactory(elements.HR));
        this.appendChild(image);
        this.appendChild(new ElementFactory(elements.P, '', party));
        this.appendChild(new ElementFactory(elements.P, '', 'Date of Birth: ' + data.date_of_birth));
        this.appendChild(new ElementFactory(elements.P, '', 'Seniority: ' + data.seniority));
        this.appendChild(new ElementFactory(elements.P, '', 'District: ' + data.district + ' and State: ' + data.state));
        if(data.in_office === 1){
            this.appendChild(new ElementFactory(elements.P, '', 'Office: ' + data.office));
            this.appendChild(new ElementFactory(elements.P, '', 'Phone number: ' + data.phone));
        }
        this.appendChild(new ElementFactory(elements.P, '', 'Twitter account handle: ' + data.twitter_account));
        this.appendChild(new ElementFactory(elements.P, '', 'Total votes with party: ' + data.votes_with_party_pct + "%"));
        this.appendChild(new ElementFactory(elements.P, '', 'Missed votes: ' + data.missed_votes_pct + "%"));
        this.appendChild(new IconLinkElement('/assets/state/' + window.STATE_MAP[data.state.toLowerCase()], data.state, data.state))
    }
}

defineCustomElement('cit-member', CITMember);