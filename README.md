# LLMOps-Project

End-to-End implementation project for LLM following LLMOps principles

docker command for mlflow
docker pull ghcr.io/mlflow/mlflow:v2.20.2
docker run -d -p 5000:5000 --name mlflow-server ghcr.io/mlflow/mlflow mlflow server --host 0.0.0.0 --port 5000
