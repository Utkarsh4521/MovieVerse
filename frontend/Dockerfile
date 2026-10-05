# ─── Frontend Dockerfile ─────────────────────────────────────────────
FROM node:20-alpine

WORKDIR /app

# Install dependencies first (layer-cached separately from source code).
COPY package.json package-lock.json ./
RUN npm ci

# Copy application source.
COPY . .

EXPOSE 5173

# Vite dev server — binds to 0.0.0.0 so Docker port mapping works.
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]