var Vue = require("vue");

Vue.component('list-item', {
  props: ['data'],
  template: `
    <div class="list-item-container">
      <div class="row top-row">
         <a :href="data.ad.url" class="list-item-link">
           <div class="no-image">
             <span class="uppercase">Kohteesta<br> ei ole kuvaa</span>
           </div>
           <ul class="list-unstyled">
             <li class="semi-bold">{{ data.house.size }}</li>
             <li class="semi-bold">{{ data.house.type }}</li>
             <li class="visible-xs">{{ data.house.address }}</li>
             <li class="rent">
               <span class="price">{{ data.house.price }}</span>
             </li>
           </ul>
         </a>
       </div>
    </div>`
});

Vue.component('pagination', {
  props: ['data'],
  template: `
    <ul class="pagination">
	    <li>
	      <a class="list-pager-button" href="#" style="cursor: default;">Edellinen</a>
	    </li>
	    <li>
	      <span>Sivu:</span>
	    </li>
      <li class="active"><a href="#">1</a></li>
      <li><a :href="data.urls[0]">2</a></li>
      <li><a :href="data.urls[1]">3</a></li>
      <li><span class="no-wrap pad-left-0 pad-right-0">...</span></li>
      <li><a :href="data.urls[2]">5</a></li>
      <li>
        <a class="list-pager-button" :href="data.urls[0]">Seuraava</a>
      </li>
    </ul>
  `
});

const pages = {
  pages: {
    urls: ['2', '3', '4']
  }
};

var top_pagination = new Vue({
  el: '#top-pagination',
  data: pages
});

var bottom_pagination = new Vue({
  el: '#bottom-pagination',
  data: pages
});

var items = new Vue({
  el: '#items',
  data: {
    ads: [
      {
        id: 0,
        ad: {
          url: '/vuokra-asunto/1'
        },
        house: {
          size: 'kerrostalo, 10 m²',
          type: 'Omahuone',
          address: 'Helsinki, Foobarintie 10',
          price: '575 €/kk'
        }
      },
      {
        id: 1,
        ad: {
          url: '/vuokra-asunto/2'
        },
        house: {
          size: 'kerrostalo, 30 m²',
          type: 'Vuokra-asunto',
          address: 'Helsinki, Foobarintie 12',
          price: '975 €/kk'
        }
      },
      {
        id: 2,
        ad: {
          url: '/vuokra-asunto/3'
        },
        house: {
          size: 'kerrostalo, 50 m²',
          type: 'Vuokra-asunto',
          address: 'Helsinki, Foobarintie 14',
          price: '1575 €/kk'
        }
      }
    ]
  }
});
