import cv2
from skimage.metrics import structural_similarity as ssim
import statistics


def match1(original_path_list, sample_path):

    sample_img = cv2.imread(sample_path)
    # turn images to grayscale
    sample_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)
    # resize images for comparison
    sample_img = cv2.resize(sample_img, (300, 300))
    # display  images
    cv2.imshow("sample image", sample_img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    two_dim_image_list=[]
  
    imgg=original_path_list

    for i in range(0, len(original_path_list)):
        for j in range(0,len(original_path_list[0])):
            if(j==0):
                imgg[i][j]= cv2.imread(original_path_list[i][j])
                
        
    # print(imgg)
   


    for i in range(0, len(original_path_list)):
        for j in range(0,len(original_path_list[0])):
            if(j==0):
                imgg[i][j] = cv2.cvtColor(imgg[i][j], cv2.COLOR_BGR2GRAY)

    for i in range(0, len(original_path_list)):
        for j in range(0,len(original_path_list[0])):
    # #         # resize images for comparison
            if(j==0):
                imgg[i][j] = cv2.resize(imgg[i][j], (300, 300))

    two_dim_image_list=imgg
 
           

    # #print(two_dim_image_list)
    

    similarity_value_list = average_ssim(two_dim_image_list, sample_img)
    

    return similarity_value_list



def average_ssim(two_dim_image_list, sample_img):
    total_ssim = 0
    pairs_count = 0
   
    two_dim_percent_list=[]
    # percent_list=[]
    # Compute SSIM for all pairwise combinations
    for i in range(0,len(two_dim_image_list)):  #responsibility to take over to next list inside 2d list
        percent_list=[]
        for j in range(0, len(two_dim_image_list[0])):
            if(j==0):
                ssim_score = ssim(sample_img, two_dim_image_list[i][j])*100
                percent_list.append(round(ssim_score, 2))
                percent_list.append(two_dim_image_list[i][1])
        two_dim_percent_list.append(percent_list)
                # total_ssim += ssim_score
                # pairs_count += 1
    print(two_dim_percent_list)
        # two_dim_percent_list.append(percent_list)
    # avg_ssim=statistics.mean(percent_list)
    #print(two_dim_percent_list)
    #print(len(two_dim_percent_list))

    return two_dim_percent_list




# def compute_ssim(sample_img, img2):
#     ssim = cv2.SSIM(sample_img, img2)
#     return ssim