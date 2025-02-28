#the stored model artifact in S3 should be a .tar.gz compressed model format
#!/bin/bash
tar -czvf xgboost_model.tar.gz xgboost_model.joblib