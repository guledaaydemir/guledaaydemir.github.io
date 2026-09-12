/* ==========================================================================
   ATHA — Site-wide structured data
   Injects WebSite and Organization JSON-LD once per page so individual pages
   only declare what is unique to them. Page-level JSON-LD always wins.
   ========================================================================== */
(function () {
  'use strict';

  var A = window.ATHA;
  if (!A) { return; }
  if (document.querySelector('script[data-atha-seo]')) { return; }

  var SITE = 'https://guledaaydemir.github.io/atha/';

  var graph = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'WebSite',
        '@id': SITE + '#website',
        name: 'ATHA',
        alternateName: 'ATHA — Breathe now',
        url: SITE,
        description: 'ATHA is a breathing and mindfulness app for iPhone and Apple Watch. Guided breathing for sleep, stress, focus and energy.',
        inLanguage: 'en',
        publisher: { '@id': SITE + '#developer' }
      },
      {
        '@type': 'Person',
        '@id': SITE + '#developer',
        name: 'Gül Eda Aydemir',
        jobTitle: 'Independent iOS developer',
        url: A.config.developerSite,
        email: 'mailto:' + A.config.email,
        sameAs: [A.config.developerSite]
      }
    ]
  };

  var node = document.createElement('script');
  node.type = 'application/ld+json';
  node.setAttribute('data-atha-seo', 'true');
  node.textContent = JSON.stringify(graph);
  document.head.appendChild(node);
})();