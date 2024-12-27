<script setup>
    import { useThemeStore } from '@/stores/theme';

    const themeStore = useThemeStore();   
</script>

<template>
    <div>
        <i class="bi" :class="themeStore.isDarkMode ? 'bi-moon-stars-fill' : 'bi-sun-fill'" @click="themeStore.toggleDarkMode"></i>
    </div>
</template>

<style lang="css" scoped>
    i {
        cursor: pointer;
    }
</style>