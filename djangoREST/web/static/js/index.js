window.URLS = {
        productsAll: () => '/api/products/',
        productDetails: (id) => `/api/products/${id}/`,
    };

    const getAllProducts = () => {
        const {productsAll} = window.URLS;
        return fetch(productsAll())
            .then(response => response.json())
    };

    const getProductDetails = (id) => {
        const {productDetails} = window.URLS;
        return fetch(productDetails(id))
            .then(response => response.json());
    }

    const renderProductsList = (products) => {
        let productsListItems = '';
        for (const product of products) {
            productsListItems += `
<li>
    <a class="btn-show-product-details" data-product-id="${product.id}" href="#">${product.name}</a>
</li>
            `;
        }

        return `
<ul>
${productsListItems}
</ul>`
    };

    const renderProductDetails = (product) => `
    <h2>${product.name}</h2>`

    const loadProductsList = () => {
        getAllProducts()
            .then(products => renderProductsList(products))
            .then(productsList => {
                document.querySelector('.list-products').innerHTML = productsList;
            });
    };

    const loadProductDetails = (id) => {
        getProductDetails(id)
            .then(product => renderProductDetails(product))
            .then(productDetails => {
                document.querySelector('.details-products').innerHTML = productDetails;
            });
    };

    const attachEvents = () => {
        document.body.addEventListener('click', (ev) => {
            const element = ev.target;
            if (element.classList.contains('btn-show-product-details')) {
                const productId = element.getAttribute('data-product-id');
                loadProductDetails(productId);
            }
        });
    };

    loadProductsList();
    attachEvents();