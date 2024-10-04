# PackageRoutingProgram

Application that uses a Nearest Neighbor Algorithm to efficiently route the delivery of 40 packages to their respective destinations via three trucks. The packages are sorted using a hash map, ensuring fast look-up times for various package details such as status (delivered, en route, or at the hub) and truck assignment. The tool calculates the total mileage of the delivery route and allows users to query the delivery status of packages by entering a specific time or package ID.

**Features**
- Nearest Neighbor Algorithm: Efficiently determines the shortest delivery route for 40 packages across three trucks
- Package Lookup: Check the delivery status of packages (delivered, en route, or still at the hub) at a specific time
- Truck Assignment: Displays which truck each package is assigned to
- Total Mileage Calculation: Displays the total mileage of all delivery routes
- Hash Map: Packages are stored in a hash map for optimized look-up and management
