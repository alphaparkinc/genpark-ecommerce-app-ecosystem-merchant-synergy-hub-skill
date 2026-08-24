from client import EcommerceAppEcosystemMerchantSynergyHubClient

def main():
    client = EcommerceAppEcosystemMerchantSynergyHubClient()
    res = client.audit_merchant_app_stack('cleanbeauty.com', ['SMS_Marketing', 'Page_Speed_Booster', 'Returns_Center'])
    print('Audit: ' + res['audit_id'] + ' for ' + res['store_domain'])
    print('Monthly Savings: +$' + str(res['consolidated_suite_saving_monthly_usd']) + '/mo | Latency: -' + str(res['app_api_overhead_latency_reduction_ms']) + 'ms')
    print('Synergy Score: ' + str(res['cross_app_data_synergy_score']) + '/100 | Unified Dashboard: ' + str(res['all_in_one_unified_dashboard_ready']))

if __name__ == '__main__':
    main()
