## Architechture
lpips_type = 'vgg'
first_inv_type = 'w'
optim_type = 'adam'

## Locality regularization
latent_ball_num_of_samples = 1
locality_regularization_interval = 1
use_locality_regularization = False
regulizer_l2_lambda = 0.1
regulizer_lpips_lambda = 0.1
regulizer_alpha = 30

## Loss
pt_l1_lambda = 1
pt_l2_lambda = 1
pt_lpips_lambda = 1
pt_lpips_layers = [0, 1, 2, 3, 4]

## Steps
LPIPS_value_threshold = 0.06
L2_value_threshold = 0.03
max_pti_steps = 350
first_inv_steps = 450
max_images_to_invert = 30

## Optimization
n_avg_samples = 10000
pti_learning_rate = 3e-4
first_inv_lr = 5e-3
train_batch_size = 1
use_last_w_pivots = False
