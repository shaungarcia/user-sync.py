## Layout Your Adobe Products, Product Configurations, and User Groups

[Previous Section](layout_orgs.md) | [Back to Contents](Contents.md) |  [Next Section](decide_deletion_policy.md)

Product Configurations (PCs) are group-like structures in the Adobe user management system.  Each PC is associated with a product you have purchased.  Users added to a PC are granted access to and get a license to use the corresponding product.  (The user does not receive anything in this process other than an optional notification that access has been granted.  All license management is handled by back-end systems).

When you create a PC (which is done in the Adobe Admin Conosle), you can add custom options that control how users will use the specific Adobe product.

You can add users directly to PCs to grant them access to products.  This is the most common way Adobe product licenses are managed.

Adobe User groups can be used to group users in a logical way that matches your understanding of how they are organized.  The use of user groups is optional.  User groups can then be added to PCs to grant licenses to users.  Adding users to user groups does not grant licenses unless the user group is added to a PC, making members of the user group implicitly members of the PC.


User groups and PCs can only be managed by one User Sync instance.  If there are multiple directories or distributed departments feeding user information to Adobe via User Sync, each must be matched to a single user group or PC.  Otherwise, User Sync cannot distinguish between users who should be removed and users who were added by another instance of User Sync.

You can use User Sync to manage PC membership and license allocation.  This is optional however.  You can also do this management manually on the Adobe Admin Console or using another application.

User Sync helps you manage Adobe product licenses by allowing you to place users into directory groups using the directory system interface or other tools.  Those groups are then mapped to Adobe user groups or PCs.  The mapping is part of the User Sync configuration file.  When User Sync detects that directory users are in one of these mapped groups, the user is added to the corresponding Adobe user group or PC.  Similarly, users in the user group or PC but not in the corresponding directory group are removed from the user group or PC.

&#9744; Decide if you will manage license allocation using User Sync.  If not, you can skip the remaining steps for now, but you will still need to do them and manually add users to the user groups or PCs later using the Adobe Admin Console. 

&#9744; Create the PCs in the Adobe Admin console for the configurations of products and groups of users you will be managing.

&#9744; If you are going to use User Groups, create them and add them to the PC(s) representing product licenses to be issued to members of the user group.

&#9744; Draw a diagram of your Adobe organizations, and the products and PCs in each.  Add the directory and directory groups to the picture and show the mapping.  For example:

![img](images/layout_products_map.png)





[Previous Section](layout_orgs.md) | [Back to Contents](Contents.md) |  [Next Section](decide_deletion_policy.md)
