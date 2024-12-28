<script setup>
    import { onMounted } from 'vue';

    import { useThemeStore } from './stores/theme';
    const themeStore = useThemeStore();

    import BitcoinPrice from './components/BitcoinPrice.vue';
    import DarkModeSwitcher from './components/DarkModeSwitcher.vue';

    onMounted(() => {
        themeStore.initializeTheme();
    });  
</script>

<template>
    <div class="top">
        <DarkModeSwitcher/>
    </div>
    <div class="main">
            <h1>WebScraper v0.1</h1>
            <BitcoinPrice />
    </div>
</template>

<style>
    :root {
        --topHeight: 60px;
    }

    body, html, #app {
        min-width: 100svw;
        min-height: 100svh;
    }

    .top {
        height: var(--topHeight);
        display: flex;
        justify-content: end;
        align-items: center;
        padding: 10px;
    }

    .main {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: calc(100svh - var(--topHeight));
    }
</style>
