const searchBar = document.getElementById('search-bar');
const searchButton = document.getElementById('search-btn');
const resultList = document.getElementById('results-list');
const searchContainer = document.querySelector('.search-container');

searchButton.addEventListener('click', search);
searchBar.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
    search();
  }
});

async function search() {
  const searchTerm = searchBar.value;
  if (searchTerm) {
    searchContainer.style.position = 'fixed';
    searchContainer.style.top = '0';
    searchContainer.style.left = '50%';  
    searchContainer.style.width = '50%';  
    searchContainer.style.transform = 'translate(-50%, 0)'; 
    const resultsHeight = resultList.offsetHeight; 
    searchContainer.style.height = resultsHeight + 100 + 'px';

    const resultsContainer = document.createElement('div');
    resultsContainer.classList.add('results-container');

    try {
      const response = await fetch(`/search?q=${encodeURIComponent(searchTerm)}`);
      const results = await response.json();

      resultList.innerHTML = ''; 
      resultList.style.display = 'block';
      searchContainer.style.marginTop = '100px'; 

      results.forEach(result => {
        const listItem = document.createElement('li');
        listItem.className = 'result-item';
        listItem.innerHTML = `
          <h2>${result.name}</h2>
          <p>${result.description}</p>
          <a href="${result.url}">${result.url}</a>
          <p>Category: ${result.category}</p>
          <p>Country: ${result.country}</p>
        `;
        resultList.appendChild(listItem);
      });
      document.body.appendChild(resultsContainer);
    } catch (error) {
      console.error('Error fetching search results:', error);
    }
  }
}