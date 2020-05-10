class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
          if(coordinates.length>2)
        {
            
            float diffx = coordinates[0][0]-coordinates[1][0];
            float diffy = coordinates[0][1]-coordinates[1][1];
            
            //slope is infinite i.e. line is parallel to y-axis
            if(diffx == 0) 
            {
                //for every point value of x coordinate should be same
                for(int idx = 2; idx<coordinates.length; idx++)
                {
                    if(coordinates[idx][0]!=coordinates[0][0]) return false;
                }
            }
            else
            {
                float slope = diffy/diffx;
                
                //for every two points slopes should be equal 
                for(int idx = 2; idx<coordinates.length; idx++)
                {
                    float dx = coordinates[idx][0]-coordinates[0][0];
                    float dy = coordinates[idx][1]-coordinates[0][1];
                             
                    if(slope != (dy/dx)) return false;
                }
            }
        }
        return true;
    }
}