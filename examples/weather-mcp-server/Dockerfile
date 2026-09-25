# ☔ Weather Buddy MCP: remote (Streamable HTTP) container
#   docker build -t weather-buddy-mcp .
#   docker run -p 3000:3000 -e MCP_AUTH_TOKEN=change-me weather-buddy-mcp
FROM node:22-slim
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm install --omit=dev --no-audit --no-fund
COPY server.mjs ./
ENV PORT=3000
EXPOSE 3000
USER node
CMD ["node", "server.mjs", "--http"]
