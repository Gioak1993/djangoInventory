function changeMainImage(imageUrl) {
    document.getElementById('main-image').innerHTML = '<img src="' + imageUrl + '" alt="Main Image">';
}


// function fullSizePic(imageUrl) {
//     var mainImage = document.getElementById('main-image')
//     mainImage.src = imageUrl;
//     mainImage.style.width = '500px'; // Adjust this value as needed
//     mainImage.style.height = '500px'; // Adjust this value as needed
//     document.addEventListener('click', function(event) {
//         if (!mainImage.contains(event.target)) {
//             // If the click is outside the main image, reset the image to its original size
//             mainImage.src = '{{MEDIA_URL}}{{productinfo.images.all.0.image_url}}';
//             mainImage.style.width = 'auto';
//             mainImage.style.height = 'auto';
//         }
//     });
// }