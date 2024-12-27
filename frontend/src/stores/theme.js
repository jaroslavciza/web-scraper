import { defineStore } from 'pinia';
import { ref } from 'vue'

export const useThemeStore = defineStore('theme', () => {
    const isDarkMode = ref(null);

    // Inicializace režimu podle systému
    const initializeTheme = () => {
      const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      isDarkMode.value = systemPrefersDark;

      //při změně nastavení systému, přepne režit v aplikaci
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (isDarkMode.value === null) {
            isDarkMode.value = e.matches;
        }
      });

      updateThemeClass();
    };

    const toggleDarkMode = () => {
        isDarkMode.value = !isDarkMode.value;
        updateThemeClass();
    };

    const updateThemeClass = () => {
        if (isDarkMode.value) {
          document.body.setAttribute('data-bs-theme', 'dark');
        } else {
          document.body.setAttribute('data-bs-theme', 'light');
        }
      };    

    return { isDarkMode, initializeTheme, toggleDarkMode }
});
