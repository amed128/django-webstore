// console.log("Hello world")


var updadateBtns = document.getElementsByClassName("update-cart")

for (var i=0; i < updadateBtns.length; i++){
    updadateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        console.log('User is: ', user)
        if (user==='AnonymousUser'){
            console.log('You are not logged in ...')
            alert('You must login to add to cart!')
        }else{
            updateUserOrder(productId, action)
            // console.log('The product id is: ', productId)
            // console.log('The action is: ', action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is logged in, sending data...')
    var url = '/client/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action,
        })
    })
    .then((response) => {
        return response.json()
        })
    .then((data) => {
        console.log('data: ', data)
        location.reload()
    })
}