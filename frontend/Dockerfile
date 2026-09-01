FROM node:18-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

# Nginx template to dynamically use $PORT provided by Render
RUN mkdir -p /etc/nginx/templates && \
    echo 'server { listen ${PORT}; location / { root /usr/share/nginx/html; index index.html index.htm; try_files $uri $uri/ /index.html; } }' > /etc/nginx/templates/default.conf.template

ENV PORT=80

CMD ["nginx", "-g", "daemon off;"]
