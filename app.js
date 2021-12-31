const image_div = document.createElement("img")


    fetch('assets/image_list.json')
    .then(function(response) {
      if (!response.ok) {
        throw new Error("HTTP error, status = " + response.status);
      }
      return response.json();
    })
    .then(function(json) {
      for(var i = 0; i < json.data.length; i++) {
        const path = json.data[i].img;
        console.log(path)
        image_div.setAttribute("src", path)

        document.body.appendChild(image_div);
      }
    })

    console.log("all right3");



