FROM zenika/kotlin

RUN apt update && apt install -qy make nano

COPY . /app
WORKDIR /app

CMD ["/bin/bash"]