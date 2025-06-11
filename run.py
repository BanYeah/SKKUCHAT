import argparse

from utils.Crawler import Crawler
from utils.QueryGen import QueryGen
# from utils.ResponseGen import ResponseGen
# from utils.build_dataset import build_dataset

def main(args):
    if args.mode == "prepare":
        Crawler(max_pages=10, save2DB=False)
        QueryGen()

    if args.model == "bm25":
        if args.mode == "train":
            print("This model does not require training.")
        # elif args.mode == "eval":
        #     eval_bm25(args.k) # hitrate
    elif args.model == "rag":
        if args.mode == "prepare":
            pass
            # ResponseGen.generate_response(notices, queries)
            # build_dataset.build_dataset(notices, ResponseGen.get_response())
        elif args.mode == "train" or args.mode == "eval":
            print("Training/Evaluation is not supported yet. This feature will be added in a future version.")


# 사용법
# python run.py -mode=MODE -model=MODEL -k=K
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-mode", help=" : select running mode (prepare, train, eval)") 
    parser.add_argument("-model", help=" : select model (bm25, rag)")
    parser.add_argument("-k", type=int, help=" : top-k in evaluation", default=3) 

    # argument valid check
    args = parser.parse_args()
    if args.mode not in ["prepare", "train", "eval"] or args.model not in ["bm25", "rag"]:
        print("Invalid argument.")
        exit(1)

    main(args)
