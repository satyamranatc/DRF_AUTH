let noteForm = document.getElementById("noteForm")

noteForm.addEventListener("submit", (e) => {
    e.preventDefault();

    let Title = document.getElementById("title").value
    let description = document.getElementById("description").value
    let Img = document.getElementById("ImageUrl").value

    let Data = {
        title: Title,
        description: description,
        image: Img
    }

    async function SendData()
    {
        let Res =  await axios.post("http://127.0.0.1:8000/api/createCard/",Data)

    }
    SendData();

})