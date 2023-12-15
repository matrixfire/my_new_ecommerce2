// Start with first news
let counter = 1;

// Load news 20 at a time
const quantity = 20;

// When DOM loads, render the first 20 news
document.addEventListener('DOMContentLoaded', load);

// If scrolled to bottom, load the next 20 news
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

// Load next set of news
function load() {

    // Set start and end news numbers, and update counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    // Get new news and add news
    fetch(`/get-news?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.news.forEach(add_news);
    })
};

// Add a new news with given contents to DOM
function add_news(contents) {

    // Create new news
    const news = document.createElement('div');
    news.className = 'news';
    news.innerHTML = contents;

    // Add news to DOM
    document.querySelector('#news').append(news);
};