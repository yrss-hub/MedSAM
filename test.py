import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
# 加载nii.gz文件
file_path = r'/home/scxyy3/yrss/Dataset/amos22/amos22/imagesVa/amos_0008.nii.gz'          # 替换为您的文件路径
img = nib.load(file_path)

# 获取图像数据
data = img.get_fdata()

# 查看图像的基本信息
print(f"Shape of the image data: {data.shape}")
print(f"Shape of the image data: {type(data)}")
print(f"Data type of the image: {data.dtype}")

# 显示中间切片作为示例
num = data.shape[2]
print(np.unique(data))
for i in range(num):
    plt.imshow(data[:, :, i], cmap='gray')
    plt.title(f'Slice number {i}')
    plt.axis('off')             # 关闭坐标轴
    plt.show()

# 显示中间切片作为示例
# num = data.shape[2]
# print(np.unique(data))
# for i in range(num):
# plt.imshow(data[:, :, 49], cmap='gray')
# plt.title(f'Slice number {50}')
# plt.axis('off')             # 关闭坐标轴
# plt.show()