from matplotlib import pyplot as plt
#plt.style.use("fivethirtyeigth")

slices = [153836,55126,87193,147411,104330]
labels = ['JavaScript', 'HTML/CSS', 'NODEjs', 'Python', 'Java']
#explode
explode=[0.05,0.05,0.05,0.3,0.05]


plt.pie(slices,labels=labels,explode=explode,shadow=True,
        startangle=90,autopct='%1.1f%%',
        wedgeprops={'edgecolor':'black'})

plt.title("Pulic Repositories on github")
plt.tight_layout()
plt.savefig('p1.png')
plt.show()