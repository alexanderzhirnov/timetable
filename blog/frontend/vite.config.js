import { defineConfig } from 'vite';
import path from "path";

export default defineConfig({
  build: {
    outDir: '../static/frontend',
    lib: {
      entry: path.resolve(__dirname, "src/main.ts"),
      name: "MyCssLib",
    }
  },
});