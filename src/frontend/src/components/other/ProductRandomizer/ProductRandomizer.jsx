import { useCart } from "/src/contexts/CartContext";

const getRandomProducts = (excludedProductID, amount) => {
    const { products } = useCart();

    const shuffled = [...products].sort(() => 0.5 - Math.random());
    let randomProducts = shuffled.slice(0, amount);
    randomProducts = randomProducts.filter(product => product.id !== excludedProductID);

    return randomProducts;
}

export default getRandomProducts;