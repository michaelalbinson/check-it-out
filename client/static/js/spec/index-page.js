'use strict';


class IndexPage extends _BaseDOM {
    constructor() {
        super();

        this.bootstrapStyles(true);
        this.addStyle('/alb-css/input/form.css');
        this.addStyle('/alb-css/input/input.css');

        this.appendChild(new ElementFactory(elements.H1, 'fancy', 'Where\'s That Bill?'));
        this.appendChild(new ElementFactory(elements.HR));
        this.appendChild(new ElementFactory(elements.SPAN, '', 'The site for confused people who just want to know who to yell at about that one bill you should be outraged about.'))

        // this.appendChild(new ElementFactory(elements.BR));
        // this.appendChild(new ElementFactory(elements.BR));


    }


}

customElements.define('index-page', IndexPage);