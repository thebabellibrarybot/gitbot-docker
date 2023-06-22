# Use an official Node.js runtime as the base image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the React app's source code to the container
COPY . .

# Build the production-ready React app
RUN npm run build

# Set the command to run the React app when the container starts
CMD ["npm", "start"]
