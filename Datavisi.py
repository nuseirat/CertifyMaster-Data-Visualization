import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['General', 'Security', 'Databases']
course_counts = [96, 8, 7]

# Expiration data (estimated from the dataset)
expiration_types = ['Unknown', 'Unlimited', 'Limited Time']
expiration_counts = [80, 25, 6]  # Estimated counts

# Top providers (estimated from the dataset)
providers = ['Cisco', 'RedHat', 'Google', 'AWS', 'Others']
provider_counts = [10, 12, 8, 6, 75]  # Estimated counts

# Create a figure with 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 18))

# 1. Courses by Category
ax1.bar(categories, course_counts, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
ax1.set_title('Number of Free Courses by Category', fontsize=16)
ax1.set_xlabel('Category', fontsize=12)
ax1.set_ylabel('Number of Courses', fontsize=12)
for i, count in enumerate(course_counts):
    ax1.text(i, count, str(count), ha='center', va='bottom')

# 2. Courses by Expiration Type
ax2.pie(expiration_counts, labels=expiration_types, autopct='%1.1f%%', startangle=90)
ax2.set_title('Distribution of Courses by Expiration Type', fontsize=16)

# 3. Top Providers
y_pos = np.arange(len(providers))
ax3.barh(y_pos, provider_counts, align='center')
ax3.set_yticks(y_pos)
ax3.set_yticklabels(providers)
ax3.invert_yaxis()  # labels read top-to-bottom
ax3.set_title('Number of Courses by Top Providers', fontsize=16)
ax3.set_xlabel('Number of Courses', fontsize=12)
for i, v in enumerate(provider_counts):
    ax3.text(v + 0.5, i, str(v), va='center')

plt.tight_layout()
plt.show()
