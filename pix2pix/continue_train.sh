python train.py --dataroot ./datasets/$1 --name $2 --model pix2pix --which_model_netG unet_1024 --loadSize 1054 --fineSize 1024 --which_direction AtoB --lambda_A 100 --dataset_mode aligned --no_lsgan --norm batch --pool_size 0 --display_freq 20 --continue_train
