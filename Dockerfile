FROM mongo:4.4

# Optional: Set up custom MongoDB configurations if needed
COPY mongod.conf /etc/mongod.conf

CMD ["mongod", "--bind_ip_all"]
