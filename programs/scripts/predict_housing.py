"""Local inference demonstration with the saved complete housing pipeline."""
import argparse
import json
import cloudpickle
import pandas as pd
from mlcourse.common import DATA, OUT

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', help='CSV with the nine original feature columns')
    args = parser.parse_args()
    model_path = OUT/'models/housing_pipeline.pkl'
    if not model_path.exists():
        raise SystemExit('先執行 Notebook 02，產生本機模型。')
    with model_path.open("rb") as file:
        model = cloudpickle.load(file)
    metadata = json.loads((model_path.parent/'housing_metadata.json').read_text())
    if args.csv:
        frame = pd.read_csv(args.csv)
    else:
        frame = pd.read_csv(DATA/'housing.csv').head(5)
    missing = set(metadata['raw_features']) - set(frame.columns)
    if missing:
        raise ValueError(f'Missing input columns: {sorted(missing)}')
    prediction = model.predict(frame[metadata['raw_features']])
    print(json.dumps({'predictions_USD':prediction.tolist(), 'rows':len(prediction)},indent=2))

if __name__ == '__main__':
    main()
