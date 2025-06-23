FROM golang:1.21 AS builder

WORKDIR /app

COPY go.mod .
COPY main.go .

# Сборка без cgo, под linux/amd64
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o server

FROM alpine:latest

WORKDIR /root/
COPY --from=builder /app/server .
RUN chmod +x ./server

EXPOSE 8080
CMD ["./server"]

