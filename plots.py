import matplotlib.pyplot as plt

def source_image_planes(stack,transformed,
                simplices,
                realpos,image,
                lowerend,upperend,
                caustics=False):
    '''Uses 'matplotlib' library to view the image and source plane, the triangulization mesh, critical curves, caustics, image and source position.'''
    
    if caustics:
        [critx,crity],[causticsx,causticsy] = caustics

    plt.subplot(1,2,1) # image plane
    plt.title('Image Plane')
    plt.axis([lowerend,upperend,lowerend,upperend])
    plt.gca().set_aspect('equal', adjustable='box') # equal ratios on x and y axis
    
    if caustics:
        plt.scatter(critx,crity, color='red', s=1, zorder=2) # plot of critical curve(s)

    plt.triplot(stack[:,0],stack[:,1], simplices, color='blue', zorder=1) # plot of the Delaunay Triangulization
    
    plt.scatter(*zip(*realpos), marker='*', color='green', s=100, zorder=2)

    plt.subplot(1,2,2) # source plane
    plt.title('Source Plane')
    plt.axis([lowerend,upperend,lowerend,upperend])
    plt.gca().set_aspect('equal', adjustable='box') # equal ratios on x and y axis

    plt.triplot(transformed[:,0],transformed[:,1], simplices, color='blue', zorder=1) # plot of the transformed Delaunay Triangulization

    plt.scatter(*zip(image), marker='*', color='red', s= 100, zorder=2 ) # plot of (observed) image position
    if caustics:
        plt.scatter(causticsx, causticsy, color ='green', s=1, zorder=2) # plot of caustics
    
    plt.show()
