'use strict';


class WTBPage extends AppPage {
    render() {
        this._header.setHeaderLinks([{title: 'Home', link: '/'}]);
        this._header.setHeroImage('/assets/logo.png', 'Where\'s that bill logo', 'header-img', 'header-img-wrap');
        this._header.render();

        this._footer.setCopyright('Website by Michael Albinson and Himesh Bhatia © 2017-2020');
        this._footer.setMetaLinks([{title: 'About', link: '/about'}]);
        this._footer.render();
    }
}

customElements.define('wtb-page', WTBPage);