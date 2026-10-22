/* ==========================================================================
   ATHA — Site-wide structured data (legacy fallback)
   Every published page now carries its WebSite / Person / MobileApplication
   JSON-LD as static HTML, so this script is no longer loaded by them. It is
   kept for older templates and does nothing when static JSON-LD is present.
   ========================================================================== */
(function () {
  'use strict';

  if (document.querySelector('script[type="application/ld+json"]')) { return; }

  var SITE = 'https://guledaaydemir.github.io/ATHA/';
  var PERSON = 'https://guledaaydemir.github.io/#person';

  var graph = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'WebSite',
        '@id': SITE + '#website',
        name: 'ATHA',
        alternateName: 'ATHA: Breathing Exercises',
        url: SITE,
        inLanguage: 'en',
        publisher: { '@id': PERSON }
      },
      {
        '@type': 'Person',
        '@id': PERSON,
        name: 'Gül Eda Aydemir',
        alternateName: 'Gul Eda Aydemir',
        jobTitle: 'Independent iOS developer',
        url: 'https://guledaaydemir.github.io/about/',
        email: 'mailto:solostaseraofficial@gmail.com',
        sameAs: [
          'https://apps.apple.com/us/developer/gul-eda-aydemir/id1889159460',
          'https://instagram.com/solo.stasera'
        ]
      }
    ]
  };

  var node = document.createElement('script');
  node.type = 'application/ld+json';
  node.setAttribute('data-atha-seo', 'true');
  node.textContent = JSON.stringify(graph);
  document.head.appendChild(node);
})();
