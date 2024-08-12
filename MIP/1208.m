image = imread('download.jpg');
im = imshow(image)

grey_img = im2gray(image)
imshow(grey_img)

filter = [-1 -1 -1,0 0 0, 1 1 1];
R = image(:,:,1);
G = image(:,:,2);
B = image(:,:,3);
redE = filter2(filter,R)
greenE = filter2(filter,G)
blueE = filter2(filter,B)

imshow(redE)

imshow(greenE)

imshow(blueE)

imwrite(R,'R.jpg')
imwrite(G,'G.jpg')
imwrite(B,'B.jpg')

imgf = imfinfo('download.jpg')
imageinfo(im,imgf)
