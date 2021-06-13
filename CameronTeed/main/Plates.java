package com.breakfast.main;

public class Plates extends HitBoxes {

    private final int param1 = 514;
    private final int param2 = 190;
    private final int param3 = 175;
    private final int param4 = 150;
    private final int param5 = 375;
    private final int param6 = 550;
    

    public boolean isHit(final int x, final int y) {
        if (isClicked(x, y, param1, param2, param3, param4)) {
            
            return true;
        } else {
            return false;
        }
    }

    public boolean isHit2(final int x, final int y) {
        if (isClicked(x, y, param5, param2, param3, param4)) {
            
            return true;
        } else {
            return false;
        }
    }

    public boolean isHit3(final int x, final int y) {
        if (isClicked(x, y, param6, param2, param3, param4)) {
            
            return true;
        } else {
            return false;
        }
    }
}
