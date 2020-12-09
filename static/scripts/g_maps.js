function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: { lat: 48.922271, lng: 24.710514 },

    });

    // Display the area between the location southWest and northEast.

    // Add 5 markers to map at random locations.
    // For each of these markers, give them a title with their index, and when
    // they are clicked they should open an infowindow with text from a secret
    // message.
    const places = [
        ['24.694070,48.931982' ,'Назва вулиці', '24.694070,48.931982/form.html', '24.694070,48.931982/panorama.html'],

    ];
    const lngSpan = [24.694070];

    const latSpan = [48.931982];

    for (let i = 0; i < lngSpan.length; ++i) {
        const marker = new google.maps.Marker({
            position: {
                lat:  latSpan[i],
                lng:  lngSpan[i] ,
            },
            map: map,
        });
        var infoWindow = "<div class=''> <a href='" + places[i][2] + "'>Форма</a> <a href='" + places[i][3] + "'>Панорама</a> </div>"
        attachSecretMessage(marker,infoWindow );
    }
}

// Attaches an info window to a marker with the provided message. When the
// marker is clicked, the info window will open with the secret message.
function attachSecretMessage(marker, secretMessage) {
    const infowindow = new google.maps.InfoWindow({
        content: secretMessage,
    });
    marker.addListener("click", () => {
        infowindow.open(marker.get("map"), marker);
    });
}
