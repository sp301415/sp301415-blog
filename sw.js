// Self-destroying service worker from: https://github.com/NekR/self-destroying-sw
// Remove this file in, idk, a year maybe?

self.addEventListener('install', function (e) {
    self.skipWaiting();
});

self.addEventListener('activate', function (e) {
    self.registration.unregister()
        .then(function () {
            return self.clients.matchAll();
        })
        .then(function (clients) {
            clients.forEach(client => client.navigate(client.url))
        });
});