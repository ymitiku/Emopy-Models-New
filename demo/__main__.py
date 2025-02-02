
from keras.models import model_from_json
from . import web_cam_demo,video_demo,image_demo
import argparse 
import os




def main():
    parser = argparse.ArgumentParser()
    # --mtype is model type argument. it can be either 'np'(neutral vs positive emotion classifier) or 'ava'(All basic
    # seven emotion classifier[anger,fear,disgust,happy,sad,surprise,neutral]). Default is 'np'
    parser.add_argument("--mtype", default="np")

    # --ttype is test type. It can be either 'image','video' or 'webcam'. default is 'webcam'
    parser.add_argument("--ttype",default="webcam", type=str)

    # --path is path to either image or video. if --ttype is 'webcam' then --path argument will not be used.
    parser.add_argument("--path",default="", type=str)

    # --frame_width is frame width video or should be resized. 
    parser.add_argument("--frame_width",default=600, type=int)
    args = parser.parse_args()
    

    if not args.mtype  in ["np",'ava',"ava-ii"]:
        print "--mtype should be either np,ava or ava-ii"
        return
    if not args.ttype  in ["image","webcam",'video']:
        print "--mtype should be either image, webcam or video"
        return
    if args.ttype in ["image","video"] and not os.path.exists(args.path):
        print "invalid path for --path"
        return
    if args.ttype == "image":
        image_demo(args.mtype,args.path)
    elif args.ttype == "video":
        video_demo(args.mtype,args.path,args.frame_width) 
    else:
        web_cam_demo(args.mtype,args.frame_width);
        

if __name__ == "__main__":
    main()
    