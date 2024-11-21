let CardContainer = document.getElementById("CardContainer");

async function GetCard() {
  let Res = await axios.get("http://127.0.0.1:8000/api/getCards/");
  let CardsData = Res.data;
  Display(CardsData);
}

function Display(CardsData) {
  CardContainer.innerHTML = "";
  CardsData.forEach((card) => {
    CardContainer.innerHTML += `

          <div class = "Card">
                <img src="https://placehold.co/600x400" alt="">
                <h3>${card.name}</h3>
                <p>${card.description}</p>
                <div class = "Btns">
                    <button>View</button>
                </div>
            </div>
        
        `;
  });
}

GetCard()
