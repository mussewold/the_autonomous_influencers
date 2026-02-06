import pytest

def test_onchain_payment_contract():
    """
    Asserts that the skill_onchain_payment accepts mandatory 
    Coinbase AgentKit parameters.
    """
    from skills.skill_onchain_payment import execute_payment
    
    # Test valid contract
    valid_payload = {
        "recipient_address": "0x123...",
        "amount_usd": 50.0,
        "network": "base"
    }
    
    # This should fail because the skill is not implemented
    response = execute_payment(**valid_payload)
    assert "transaction_hash" in response

def test_social_post_constraints():
    """
    Asserts the Judge can enforce character limits via the skill interface.
    """
    from skills.skill_generate_social_post import generate_post
    
    params = {
        "platform": "twitter",
        "constraints": {"max_chars": 280}
    }
    
    # This should fail initially
    result = generate_post(params)
    assert len(result["content_draft"]) <= 280