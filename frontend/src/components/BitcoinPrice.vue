<script setup>
    import { ref, onMounted } from 'vue';

    const price = ref('');
    const loading = ref(true);
    const error = ref('');

    async function getBTCprice() {
        try {
            const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
            const response = await fetch(apiBaseUrl+'/api/btc');
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