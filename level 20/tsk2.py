import mlflow.sklearn
from sklearn.metrics import mean_squared_error,r2_score
mlflow.sklearn.autolog()
mlflow.log_metric(f'mse{mean_squared_error}')
mlflow.log_metric(f'r2{r2_score}')