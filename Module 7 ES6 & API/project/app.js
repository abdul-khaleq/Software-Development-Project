const loadData = ()=>{
    searchText = document.getElementById("search-text").value;
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?f=${searchText}`)
    .then((res)=>res.json())
    .then((data)=>displayMeals(data.meals))
}
const displayMeals = (data)=>{
    document.getElementById("total-meals").innerText = data.length;
    const mealsContainer = document.getElementById("meals-container");

    data.forEach((meal)=>{
        const card = document.createElement("div");
        card.classList.add("box");
        card.innerHTML = `
        <img class="card-img" src=${meal?.strMealThumb} alt="">
        <h1>${meal?.strMeal}</h1>
        <p>${meal?.strInstructions.slice(0,55)}</p>
        <button></button>
        `;
        mealsContainer.appendChild(card)
    });
};