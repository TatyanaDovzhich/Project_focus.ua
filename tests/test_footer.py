"""Tests related to footer"""

import pytest
import logging

from constants.base import BaseConstants

@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestFooter:
    """Stores tests for footer base functionality"""

    log = logging.getLogger("[TestFooter]")

    def test_facebook_social_link(self, footer):
        """
        - Pre-conditions:
            - Open Start Page
            - Navigate to footer
        - Steps:
            - Navigate to Facebook Page via clicking on Facebook Social Link
            - Verify result
        """
        # Navigate to Facebook Page via clicking on Facebook Social Link
        facebook_page = footer.navigate_to_facebook_page()

        # Verify result
        facebook_page.verify_to_facebook_page_successful_transition()
