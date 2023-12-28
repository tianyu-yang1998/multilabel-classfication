python net_grd_avst/main_avst.py  --mode train \
	--audio_dir ./data/audio \
	--video_res14x14_dir ./data/ \
	--wandb 0 --num_workers 32 --batch-size 32 --model_name swinv2_tune_av+vggish