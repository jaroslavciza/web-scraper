<script setup>
    import { ref, onMounted } from 'vue';

    const price = ref('');
    const loading = ref(true);
    const error = ref('');

    async function getBTCprice() {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/btc');
            const data = await response.json();
            if (data.error) {
                error.value = data.error;
            } else {
                price.value = data.price;
            }
        } catch (err) {
            error.value = 'Failed to fetch the price. Please try again later.';
        } finally {
            loading.value = false;
        }
    }

    setInterval(() => {
        getBTCprice();
    }, 60000);

    onMounted(getBTCprice);    
</script>

<template>
    <div>
        <p v-if="loading">Loading...</p>
        <p v-else-if="error">{{ error }}</p>
        <p v-else>Current Bitcoin Price: {{ price }}</p>
    </div>
</template>

<style lang="css" scoped>
p {
  font-size: 1.2em;
  margin: 10px 0;
}
</style>